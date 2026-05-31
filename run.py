import uvicorn


if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)


git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Eliasraad/haris_backend.git
git push -u origin main