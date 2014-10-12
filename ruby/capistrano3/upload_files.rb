namespace :devops do
   desc "Copy files"
   task :copy do
      on roles(:all) do |host|
         %w[ file.one file.two ].each do |f|
            upload! '/path/fo/file/' + f , '/remote/path/' + f
         end
      end
   end
end
