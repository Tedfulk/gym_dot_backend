CREATE MIGRATION m12wlxrrjl2oqwdd7z5vpbqlb2mocf7f4wjf5bi2kw4wfex5mjmtcq
    ONTO m1uishw3c256of62lsjqdmogv2ijkgyg554eueebcvk7jlddxabamq
{
  CREATE TYPE default::Classes {
      CREATE PROPERTY active -> std::bool {
          SET default := true;
      };
      CREATE PROPERTY class_dates -> array<cal::local_date>;
      CREATE PROPERTY class_tmies -> array<cal::local_time>;
      CREATE PROPERTY len_of_class_time -> std::duration;
      CREATE PROPERTY max_attendees -> std::int16 {
          CREATE CONSTRAINT std::min_value(1);
      };
  };
  CREATE TYPE default::Programs {
      CREATE MULTI LINK class -> default::Classes;
      CREATE PROPERTY active -> std::bool {
          SET default := true;
      };
      CREATE PROPERTY description -> std::str;
      CREATE REQUIRED PROPERTY name -> std::str;
  };
  ALTER TYPE default::Facilities {
      CREATE MULTI LINK program -> default::Programs;
  };
};
