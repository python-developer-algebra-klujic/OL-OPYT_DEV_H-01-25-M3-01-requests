from repositories import UsersApi


def main():
    user_api_repo = UsersApi()
    users_from_internet = user_api_repo.get_users()
    print(users_from_internet)


if __name__ == '__name__':
    main()
