# 3-10. Every Function
# Think of something you could store in a list. For example, you could
# make a list of mountains, rivers, countries, cities, languages, or
# anything else you’d like. Write a program that creates a list
# containing these items and then uses each function introduced in this
# chapter at least once.

countries = ['canada', 'peru', 'south korea', 'italy', 'germany']
print(countries)
print(countries[1])
print(countries[-1])
print(countries[2].title())
print(f"I live in {countries[0].title()}.")
countries[1] = 'argentina'
print(countries)
countries.append('peru')
print(countries)
countries.insert(1, 'iceland')
print(countries)
del countries[2]
print(countries)
countries.pop()
print(countries)
countries.remove('iceland')
print(countries)
print(sorted(countries))
print(sorted(countries, reverse=True))
countries.sort()
print(countries)
countries.sort(reverse=True)
print(countries)
countries.reverse()
print(countries)
print(len(countries))