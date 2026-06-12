# SBA – Module 3 Report: Cloud Web Application Deployment
**Student:** Baha Emir · **Group:** SD1 · **Project:** Geometry Calculator on Azure

> Paste into Word, insert the 3 screenshots, add the two links, export as **PDF**.

---

## 1. Application functionality
A distributed geometry calculator deployed to **Microsoft Azure** with a decoupled
front-end / back-end architecture:
- **Frontend (Azure Web App):** a Flask app (`app.py`) serves `index.html`, a single-page UI
  where the user picks a shape, enters dimensions, and clicks **Calculate**.
- **Backend (Azure Function, Python V2):** an HTTP-triggered function `CalculateArea`
  (`api/function_app.py`) receives a JSON body `{"shape": ..., "data": {...}}`, computes the
  area for square / rectangle / triangle / circle, and returns `{"area": ...}` as JSON.
- **Interaction:** the frontend calls the backend with `fetch()` over HTTPS. Because they live
  on different domains, **CORS** is configured on the Function App to allow the Web App origin.
- **Automation (CI/CD):** every `git push` to `main` triggers GitHub Actions, which builds and
  deploys both the Web App and the Function App automatically (Deployment Center bridge).
- **Versioning:** Git tags `v1` (frontend monolith) and `v2` (API integration) mark releases.

## 2. Required screenshots
**[SCREENSHOT a — Web App Overview]** the Azure portal Overview page of the Web App (URL visible).

**[SCREENSHOT b — Function App Overview]** the Azure portal Overview page of the Function App.

**[SCREENSHOT c — GitHub Actions]** the Actions tab showing the build/deploy workflows (green).

## 3. Links
- GitHub repository: `https://github.com/<YOUR_USERNAME>/SBA_Azure`
- Live Web App: `https://<your-webapp-name>.azurewebsites.net`

---

### Architecture note
This is the **PaaS** model: Azure manages the OS, runtime and servers; we provide only the code.
The Web App is a thin client (presentation layer); heavy logic is offloaded to the serverless
Function (business-logic layer), which scales independently per request — optimizing cost.
