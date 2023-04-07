CREATE MIGRATION m17se25ephzc6h5sd3w6gllcdzkhbctiekx4hv6hr7uhmrvbhtzvnq
    ONTO m14up4dyoh3j4growxo3w2cyvvcxry5fnoa6nwh4674qqogbr5zfna
{
  ALTER TYPE default::Facilities {
      ALTER LINK program {
          CREATE CONSTRAINT std::exclusive;
      };
  };
  ALTER TYPE default::Programs {
      ALTER LINK class {
          CREATE CONSTRAINT std::exclusive;
      };
  };
};
