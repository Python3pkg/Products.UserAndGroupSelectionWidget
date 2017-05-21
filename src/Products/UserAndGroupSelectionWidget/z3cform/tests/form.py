import zope.schema
import zope.interface
import z3c.form

from Products.UserAndGroupSelectionWidget.z3cform import widget


class ITestForm(zope.interface.Interface):

    field1 = zope.schema.TextLine(
        title="Field1",
        required=True,
        )

    field2 = zope.schema.List(
        title="Field2",
        required=True,
        )


class TestForm(z3c.form.form.Form):

    fields = z3c.form.field.Fields(ITestForm)
    fields['field1'].widgetFactory = widget.UserAndGroupSelectionFieldWidget
    fields['field2'].widgetFactory = widget.UserAndGroupSelectionFieldWidget

    ignoreContext = True

    @z3c.form.button.buttonAndHandler('Cancel')
    def handleCancel(self, action):
        print('Canceling')

    @z3c.form.button.buttonAndHandler('Save')
    def handleSave(self, action):
        data, errors = self.extractData()
        if errors:
            return False

        print('Field1: ' + data['field1'])
        print('Field2: ' + data['field2'])
