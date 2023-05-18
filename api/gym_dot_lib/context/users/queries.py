ALL_USERS = r"""
select Users {
    id,
    email,
    first_name,
    last_name,
    full_name,
    avatar_src,
    role,
    oauth_accounts: {
        id,

}
"""


CREATE_USER = r"""
select (
    insert Users {
        email := <str>$email,
        first_name := <str>$first_name,
        last_name := <str>$last_name,
        password_hash := <str>$password_hash,
        avatar_src := <str>$avatar_src,
    }
) {
    id,
    email,
    first_name,
    last_name,
    full_name,
    avatar_src,
    role,
}
"""

DELETE_USER = r"""
delete Users
    filter .id = <uuid>$user_id
"""

GET_USER_BY_ID = r"""
select Users {
    id,
    email,
    first_name,
    last_name,
    full_name,
    avatar_src,
    role,
    }
    filter .id = <uuid>$user_id
"""

GET_USER_BY_EMAIL = r"""
select Users {
    id,
    email,
    first_name,
    last_name,
    full_name,
    avatar_src,
    role,
    }
    filter .email = <str>$email
"""

UPDATE_USER = r"""
select (
    update Users
    filter .id = <uuid>$user_id
    set {
        email,
        first_name,
        last_name,
        avatar_src,
        role,
    }
) {
    id,
    email,
    first_name,
    last_name,
    full_name,
    avatar_src,
    role,
}
"""
