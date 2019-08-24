require "nokogiri"
require "httparty"


def scraper
	url = "https://mayukhdeb.github.io/"

	unparsed_page = HTTParty.get(url)

	parsed_page = Nokogiri::HTML(unparsed_page)

	arr  = Array.new   # call an array 
	

	heads = parsed_page.css('div.content')
	
	heads.each do |head_listing|   # like a loop
		head = {
			content: head_listing.css('p').text   # extracts paragraph

		}
	arr << head  # like append
	end
	File.open("saved.txt", "w+") do |f|  # saves the extracted paragraphs in a text file 
		f.puts(arr)  
	end
	
	print "Saved !! \n"

end 

scraper  #  callng the function 
