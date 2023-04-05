CREATE MIGRATION m14up4dyoh3j4growxo3w2cyvvcxry5fnoa6nwh4674qqogbr5zfna
    ONTO m15jubgtefydanxdfuudsit7m7gy6xmgfzapg4uyfajrghqkcu3coa
{
  ALTER TYPE default::Classes {
      ALTER PROPERTY len_of_class_time {
          SET default := 60;
          SET TYPE std::int32 USING (1);
      };
  };
  ALTER TYPE default::Classes {
      ALTER PROPERTY waitlist {
          SET default := 10;
      };
  };
};
