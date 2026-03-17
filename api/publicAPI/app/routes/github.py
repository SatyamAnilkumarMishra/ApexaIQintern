from fastapi import APIRouter
from app.services.github_service import getRepoStats

router = APIRouter(prefix="/github", tags=["Github API"])

@router.get("/{owner}/{repo}")
def github(owner:str,repo:str):
    return getRepoStats(owner,repo)