CREATE MIGRATION m122mpfsgpcduu5j33vpjn6lwwvs7gwyagyy6nknv2337mcbn4zw7q
    ONTO m1gxbzkeuygvolscmi4sdwj3jnvh6tsqls44np6xaaa3nvnmlivona
{
  CREATE TYPE default::AccessToken {
      CREATE REQUIRED PROPERTY created_at -> std::datetime {
          SET default := (std::datetime_current());
      };
      CREATE REQUIRED PROPERTY token -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
  };
  CREATE TYPE default::OAuthUsers {
      CREATE REQUIRED PROPERTY access_token -> std::str;
      CREATE REQUIRED PROPERTY account_email -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE REQUIRED PROPERTY account_id -> std::str;
      CREATE PROPERTY expires_at -> std::int32;
      CREATE REQUIRED PROPERTY oauth_name -> std::str;
      CREATE PROPERTY refresh_token -> std::str;
  };
  CREATE SCALAR TYPE default::Role EXTENDING enum<admin, user>;
  CREATE TYPE default::Users {
      CREATE MULTI LINK access_token -> default::AccessToken {
          ON SOURCE DELETE DELETE TARGET;
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE MULTI LINK oauth_accounts -> default::OAuthUsers {
          ON SOURCE DELETE DELETE TARGET;
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE PROPERTY avatar_src -> std::str;
      CREATE REQUIRED PROPERTY email -> std::str {
          CREATE CONSTRAINT std::exclusive;
      };
      CREATE PROPERTY first_name -> std::str;
      CREATE PROPERTY last_name -> std::str;
      CREATE PROPERTY full_name := (((.first_name ++ ' ') ++ .last_name));
      CREATE REQUIRED PROPERTY password_hash -> std::str;
      CREATE PROPERTY role -> default::Role {
          SET default := 'user';
      };
  };
};
