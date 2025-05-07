from supabase import create_client
from django.conf import settings

class UploadImgService:
    def __init__(self):
        self.supabase = create_client(settings.SUPABASE['URL'], settings.SUPABASE['KEY'])

    def upload_to_supabase(self, file_name, file_content):
        try:
            bucket = self.supabase.storage.from_(settings.SUPABASE['BUCKET_NAME'])
            response = bucket.upload(file_name, file_content)
            print(response)
            file_url = bucket.get_public_url(file_name)
            return file_url
        except Exception as e:
            raise Exception(f"Error uploading file to Supabase: {str(e)}")
