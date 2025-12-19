import os

from supabase import create_client, Client

class SupabaseStorage:
    def __init__(self):
        self.client: Client = self._get_client()

    def _get_client(self) -> Client:
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_KEY")
        return create_client(url, key)

    def upload_file(self, file, file_name: str) -> str:
        bucket_name = "doctor-documents"
        file_path = f"{bucket_name}/{file_name}"
        self.client.storage.from_(bucket_name).upload(file_path, file)
        return file_path

    def delete_file(self, file_path: str):
        bucket_name = "doctor-documents"
        self.client.storage.from_(bucket_name).remove([file_path])

def get_storage_client():
    return SupabaseStorage()
