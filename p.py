# This is a word processor for ingredients and recipes found around the internet
# It will create an already formatted, ready to use output in the console
    
# Usage : copy ingredients and steps into recipe.txt file and python will output <li>[entry]</li> as a result
# Ready to put into your odin html code.


with open ('recipe.txt', 'r') as file:
    recipe = file.read().replace('▢', '').split('\n')

    for sentences in recipe:
        if sentences == '':
            recipe.pop(recipe.index(sentences))

    for sentences in recipe:
        recipe[recipe.index(sentences)] = '<li>' + sentences + '</li>'

    for sentences in recipe:
        print(recipe[recipe.index(sentences)])