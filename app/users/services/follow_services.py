from app.advertisements.services import AdvertisementService
from app.db import SessionLocal
from app.users.exceptions import FollowExistException, ClientsFollowingsException, AdFollowingsException, \
    FollowDoesntExistException

from app.users.repositories import FollowRepository
from app.users.services import ClientService


class FollowService:

    @staticmethod
    def create(client_id: str, advertisement_id: str):
        try:
            with SessionLocal() as db:
                follow_repo = FollowRepository(db)
                if not follow_repo.get_by_client_id_and_advertisement_id(client_id=client_id,
                                                                         advertisement_id=advertisement_id):
                    return follow_repo.create(client_id=client_id, advertisement_id=advertisement_id)
                raise FollowExistException
        except Exception as exc:
            raise exc

    @staticmethod
    def get_all_by_client_id(client_id: str):
        with SessionLocal() as db:
            ClientService.get_client_by_id(client_id=client_id)
            follow_repo = FollowRepository(db)
            client_followings = follow_repo.get_all_by_client_id(client_id=client_id)
            if client_followings:
                return client_followings
            raise ClientsFollowingsException

    @staticmethod
    def get_all_by_advertisement_id(advertisement_id: str):
        with SessionLocal() as db:
            AdvertisementService.get_active_advertisement_by_id(advertisement_id=advertisement_id)
            follow_repo = FollowRepository(db)
            ad_followings = follow_repo.get_all_by_advertisement_id(advertisement_id=advertisement_id)
            if ad_followings:
                return ad_followings
            raise AdFollowingsException

    @staticmethod
    def get_by_client_id_and_advertisement_id(client_id: str, advertisement_id: str):
        with SessionLocal() as db:
            AdvertisementService.get_active_advertisement_by_id(advertisement_id=advertisement_id)
            ClientService.get_client_by_id(client_id=client_id)
            follow_repo = FollowRepository(db)
            follows = follow_repo.get_by_client_id_and_advertisement_id(client_id=client_id,
                                                                        advertisement_id=advertisement_id)
            if follows:
                return follows
            raise FollowDoesntExistException

    @staticmethod
    def delete(client_id: str, advertisement_id: str):
        try:
            with SessionLocal() as db:
                AdvertisementService.get_active_advertisement_by_id(advertisement_id=advertisement_id)
                ClientService.get_client_by_id(client_id=client_id)
                follow_repo = FollowRepository(db)
                follow_repo.delete(client_id=client_id, advertisement_id=advertisement_id)
        except Exception as exc:
            raise exc
