library("r2ddi")

dir2xml(
  path_in = "/home/soepdist/ddionrails/soep-core/v34/de/",
  path_out = "r2ddi/v34/de/",
  missing_codes = -9:-1,
  my_cores = 30)
