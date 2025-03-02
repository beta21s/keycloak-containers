from keycloak import KeycloakAdmin
import csv
import time
import random
import string

keycloak_admin = KeycloakAdmin(
    server_url="https://sso.vlute.edu.vn/auth/",
    username='admin',
    password='',
    realm_name="master",
    verify=True)

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def create_users(username, email, first_name, last_name, password):
    try:
        user_data = {
            "username": username,
            "email": email,
            "firstName": first_name,
            "lastName": last_name,
            "enabled": True,
            "credentials": [{
                "type": "password",
                "value": password,
                "temporary": False
            }]
        }

        # Thêm người dùng vào Keycloak
        keycloak_admin.create_user(user_data, exist_ok=False)
        print(f"Created user {username} successful")

    except Exception as e:
        print(f"Error creating user {i}: {str(e)}")

    # Tạm ngừng để tránh quá tải API
    time.sleep(1)