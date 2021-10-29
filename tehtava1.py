import requests
from google.cloud import storage

def read_and_write():
    sr = requests.get('https://2ri98gd9i4.execute-api.us-east-1.amazonaws.com/dev/academy-checkpoint2-json')
    data = sr.json()
    uusi = []
    for d in sorted(data['items'], key=lambda x: x['parameter']):
        uusi.append(d["parameter"])
    print(uusi)

    with open('checkpoint1.txt', 'a') as f:
        for item in uusi:
            f.write(item + "\n")
        f.close()

def create_new_bucket(bucket_name: str):
    from google.cloud import storage
    client = storage.Client()
    client.create_bucket(bucket_name)


def save_file_into_bucket(filename):
    client = storage.Client()
    bucket = client.get_bucket('kolmas_ampari1234')
    blob = bucket.blob("checkpoint1.txt")
    blob.upload_from_filename(filename)


if __name__ == "__main__":
    read_and_write()    
    create_new_bucket("kolmas_ampari1234") 
    save_file_into_bucket(filename='C:/Users/Miia/Documents/vko3-1/checkpoint.txt') 