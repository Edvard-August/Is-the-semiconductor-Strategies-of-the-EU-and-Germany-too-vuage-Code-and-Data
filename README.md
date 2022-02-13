# Are-the-semiconductor-Strategies-of-the-EU-and-Germany-too-vuage-Code-and-Data
The project deals with the structuring of R&D&I Funding data retrieved from Cordis (search term: 'Semiconductors EV' start dates: 2012 and later, organior country: Germany) into edge lists that be used for Sosial Network Analysis. Specifically, these edge lists take the form of spread sheets, and the data is treated as if the edges are directed and weighted (funding mobilized). The data is organised with help of Python Program, that is centred on around Pandas, for loops and dictionaries. It should be mentioned a part of the program is probably not needed, this part takes a file containing R&D&I funding data for the same projects, but this time retrieved through a web scraping application (Octoparse 8) and checks if the website version of the data is more extensive in cases of missing data from the Primary data set. It does not appear to be case. 
Input files:
 -organization.json (Cordis)
 -project.json (Cordis)
 -CORDIS _ European Commission - funding semi ev.xlsx
outfiles:
 -Resource_edge_list_part1r
 -Resource_edge_list_part2r
Gephi file - final SNA
 -Semicondocture EV - knowlegede development resource mobilisation network.gephi
Edvard August Eggen Sveum
FU Berlin 
5501132
