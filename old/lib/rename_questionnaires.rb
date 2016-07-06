files = Dir.entries "."
files.delete "."
files.delete ".."
files.delete "rename.rb"
files.each do |file_old|
  file_new = /soep-core-[0-9]*-[a-z0-9]*/i.match(file_old).to_s.downcase + ".xml"
  system "mv #{file_old} #{file_new}"
end
