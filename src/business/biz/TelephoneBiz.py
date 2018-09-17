from ...models.models import Telephone


class TelephoneBiz:

    def get_or_none(self, number):
        return Telephone.get_or_none(number=number)

    def save_and_get(self, number):
        exists = self.get_or_none(number)
        if not exists:
            model = Telephone(number=number, name='XXXXXXXXXXXX')
            mod = model.save(force_insert=True)
            if mod > 0:
                return self.get_or_none(number)
        return exists
