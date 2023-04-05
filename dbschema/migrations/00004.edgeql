CREATE MIGRATION m1gvh3sel5z5oawjnd3a6rv277d745o2r4bsmxxoorccddbjxjfuma
    ONTO m12wlxrrjl2oqwdd7z5vpbqlb2mocf7f4wjf5bi2kw4wfex5mjmtcq
{
  ALTER TYPE default::Classes {
      CREATE PROPERTY min_attendees -> std::int16 {
          CREATE CONSTRAINT std::min_value(1);
      };
      CREATE PROPERTY waitlist -> std::int16;
  };
};
