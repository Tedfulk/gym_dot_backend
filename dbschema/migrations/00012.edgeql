CREATE MIGRATION m1mhnr7eaiz3wc2tal4zfckyzgspfufia3ktyxg5l2et27677u54uq
    ONTO m122mpfsgpcduu5j33vpjn6lwwvs7gwyagyy6nknv2337mcbn4zw7q
{
  ALTER TYPE default::OAuthUsers {
      ALTER PROPERTY access_token {
          RENAME TO oauth_access_token;
      };
  };
  ALTER TYPE default::OAuthUsers {
      ALTER PROPERTY expires_at {
          SET default := ((std::datetime_current() + <std::duration>'24 hours'));
          SET TYPE std::datetime USING (std::datetime_current());
      };
  };
};
