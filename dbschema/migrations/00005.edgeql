CREATE MIGRATION m15jubgtefydanxdfuudsit7m7gy6xmgfzapg4uyfajrghqkcu3coa
    ONTO m1gvh3sel5z5oawjnd3a6rv277d745o2r4bsmxxoorccddbjxjfuma
{
  ALTER TYPE default::Classes {
      ALTER PROPERTY max_attendees {
          SET TYPE std::int32;
      };
  };
  ALTER TYPE default::Classes {
      ALTER PROPERTY min_attendees {
          SET TYPE std::int32;
      };
  };
  ALTER TYPE default::Classes {
      ALTER PROPERTY waitlist {
          SET TYPE std::int32;
      };
  };
};
