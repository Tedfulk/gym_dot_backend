CREATE MIGRATION m1onfapq5ylz5lc4dhlvy6c6hibnsw6r4uf5h7lmcppptufh6m4gpq
    ONTO m17se25ephzc6h5sd3w6gllcdzkhbctiekx4hv6hr7uhmrvbhtzvnq
{
  ALTER TYPE default::Classes {
      ALTER PROPERTY class_tmies {
          RENAME TO class_times;
      };
  };
};
