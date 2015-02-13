import sys
import web

urls = (
  '/calculator', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index(object):
    def GET(self):
        return render.calculator()

    def POST(self):
        form = web.input(name="yarn", greet="Hello", )
        #greeting = "%s, %s" % (form.greet, form.name)
        weight = "%s" % (form.weight)
        print "weight is", weight
        
        return render.results(results = self.compute_cost(form))
        
    def compute_cost(self,myform):
        sum = 0
        sum += (int(myform.number_of_yarn)*float(myform.cost_yarn)) 
        sum += (int(myform.number_of_needles)*float(myform.cost_needles))
        sum += (int(myform.number_of_needles2)*float(myform.cost_needles2))
        return sum
        
#         weight = "%s" % (form.weight)
#         print "weight is", weight
        #print "bonjour", greeting 
       # return render.index()
        

if __name__ == "__main__":
    app.run()
    