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
        #if (int(myform.number_of_yarn)) is not None & (float(myform.cost_yarn)) is not None: #
        sum += (int(myform.number_of_yarn)*float(myform.cost_yarn)) 
        #if int(myform.number_of_needles) is not None & float(myform.cost_needles) is not None:      #
        sum += (int(myform.number_of_needles)*float(myform.cost_needles))
        sum += (int(myform.number_of_needles2)*float(myform.cost_needles2))
        sum += (int(myform.number_of_hooks)*float(myform.cost_hooks))
        sum += (int(myform.number_of_hooks2)*float(myform.cost_hooks2))
        sum += (int(myform.number_of_buttons)*float(myform.cost_buttons))
        sum += (int(myform.quantity_supplies)*float(myform.cost_supplies))
        sum += (int(myform.quantity_supplies2)*float(myform.cost_supplies2))
        return sum
        
#         weight = "%s" % (form.weight)
#         print "weight is", weight
        #print "bonjour", greeting 
       # return render.index()
        

if __name__ == "__main__":
    app.run()
    