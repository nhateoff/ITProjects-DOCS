# Anleitung: Wie bediene ich einen Rollback, wenn die MkDocs korrupt ist?
Das hier ist eine kurze step by step Anleitung, um korrekt zur stable-version bzw. zum bisherigen "Last good known" zurückzukehren. 

## Step 1
Navigiere im Reiter auf **Actions**.
![image](../mediafiles/images/scr-navigate-actions.png)

## Step 2
In der linken Sidebar sind drei benutzerdefinierte Workflows aufzufinden. Wähle hier **"Rollback MkDocs (Deploy specific ref)"** aus.

![image](../mediafiles/images/scr-selection-rollback-mkdocs.png)

## Step 3
Es öffnet sich nun die Workflow-Übersicht. Wähle hierzu **Run workflow** aus. Danach muss die Branch **main** ausgewählt werden.
Im nächsten Feld kann grundsätzlich eine beliegebe Commit SHA/Tag ausgewählt werden. Hier verwenden wir jetzt **00_stable-version**
*Hinweis: sctrict mode sollte idealerweise auf **true** bleiben.*
![image](../mediafiles/images/scr-selection-workflow-mkdocs.png)


Owner: @nhateoff
Last reviewed: 05.04.2026
