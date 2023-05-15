# Instructions :
# Create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

# The Pagination class will accept 2 parameters:

# items (default: None): It will contain a list of contents to paginate.
# pageSize (default: 10): The amount of items to show in each page.
# So for example we could initialize our pagination like this:

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# p = Pagination(alphabetList, 4)


# The Pagination class will have a few methods:

# getVisibleItems() : returns a list of items visible depending on the pageSize
# So for example we could use this method like this:

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]
# You will have to implement various methods to go through the pages such as:
# prevPage()
# nextPage()
# firstPage()
# lastPage()
# goToPage(pageNum)

# Here’s a continuation of the example above using nextPage and lastPage:

# alphabetList = list("abcdefghijklmnopqrstuvwxyz")

# p = Pagination(alphabetList, 4)

# p.getVisibleItems() 
# # ["a", "b", "c", "d"]

# p.nextPage()

# p.getVisibleItems()
# # ["e", "f", "g", "h"]

# p.lastPage()

# p.getVisibleItems()
# # ["y", "z"]


# Notes

# The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
# The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
# Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
# If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).

class Pagination():
    def __init__(self, items = None, pageSize = 10):
        self.items = items
        self.pageSize = int(pageSize) if pageSize > 0 else 10  # Default value if pageSize is invalid
        self.totalPages = (len(self.items) - 1) // self.pageSize + 1 
        self.currentPage = 1 if self.totalPages > 0 else 0 

    def getVisibleItems(self):
        start = (self.currentPage - 1) * self.pageSize
        end = start + self.pageSize
        return self.items[start:end]

    def nextPage(self): 
        if self.currentPage < self.totalPages:
            self.currentPage += 1
        else:
            print('You are already on the last page') 
        return self   

    def prevPage(self): 
        if self.currentPage != 1:
            self.currentPage -= 1   
        else:
            print('You are on the first page') 
        return self    
    
    def firstPage(self):
        self.currentPage = 1

    def lastPage(self):
        self.currentPage = self.totalPages 

    def goToPage(self,pageNum):
        if pageNum > self.totalPages:
            self.currentPage = self.totalPages
        elif pageNum <= 0:
            self.currentPage = 1
        else:
           self.currentPage = pageNum 


alphabetList = list("abcdefghijklmnopqrstuvwxyz")
# alphabetList = list("a")
# alphabetList = []
p = Pagination(alphabetList, 4)  
print(p.getVisibleItems())  
p.nextPage().nextPage()
print(p.getVisibleItems())  
p.prevPage().prevPage()
print(p.getVisibleItems()) 
p.firstPage() 
print(p.getVisibleItems())
p.lastPage()
print(p.getVisibleItems())
p.goToPage(5)
print(p.getVisibleItems())



