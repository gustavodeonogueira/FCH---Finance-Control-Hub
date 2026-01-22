from database import get_connection
from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/transactions")
def create_transaction(description: str, amount: float):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO transactions (description, amount) VALUES (%s, %s)",
        (description, amount)
    )

    conn.commit()
    cur.close()
    conn.close()

    return {"message": "Transaction created"}

@app.get("/transactions")
def list_transactions():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, description, amount, created_at FROM transactions")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return [
        {
            "id": r[0],
            "description": r[1],
            "amount": float(r[2]),
            "created_at": r[3],
        }
        for r in rows
    ]
