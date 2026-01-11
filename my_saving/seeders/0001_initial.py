
from django_seed import Seed
from ..models import Account, Transaction  

seeder = Seed.seeder()


seeder.add_entity(Account, 10, {
    'title':    lambda x: seeder.faker.title,
    #'user': 1
})
seeder.execute()

