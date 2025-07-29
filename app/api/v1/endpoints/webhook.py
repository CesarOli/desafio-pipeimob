from fastapi import APIRouter, Body, HTTPException
import httpx

router = APIRouter(prefix="/webhook", tags=["webhook"])

WEBHOOK_URL = "https://webhook.site/95aaaf1b-a87f-4155-a193-0374b8b99dd1" 

@router.post("/")
async def forward_webhook(payload: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        response = await client.post(WEBHOOK_URL, json=payload)
    if 200 <= response.status_code < 300:
        return {"detail": "Payload encaminhado com sucesso"}
    raise HTTPException(status_code=502, detail="Falha ao encaminhar o payload")