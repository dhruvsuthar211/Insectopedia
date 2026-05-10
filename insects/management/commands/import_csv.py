import csv
from django.core.management.base import BaseCommand
from insects.models import ContentOrder, ContentFamily, ContentSpecies
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Imports real insect data from a CSV file.'

    def handle(self, *args, **kwargs):
        # Pointing to the newly updated file I made for you!
        file_path = 'real_insects.csv' 
        
        try:
            # We use windows-1252 and errors='replace' so it mathematically CANNOT crash on weird characters
            with open(file_path, newline='', encoding='windows-1252', errors='replace') as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0
                
                for row in reader:
                    # 1. Get or Create the Order
                    order, _ = ContentOrder.objects.get_or_create(
                        name=row['order_name'].strip(),
                        defaults={'common_name': f"Common {row['order_name'].strip()}"}
                    )

                    # 2. Get or Create the Family
                    family_slug = slugify(row['family_name'].strip())
                    
                    family, _ = ContentFamily.objects.get_or_create(
                        name=row['family_name'].strip(),
                        defaults={
                            'order': order,
                            'slug': family_slug
                        }
                    )

                    # 3. Create the Species
                    species_slug = row.get('slug', '').strip() or slugify(row['scientific_name'].strip())
                    
                    species, created = ContentSpecies.objects.get_or_create(
                        scientific_name=row['scientific_name'].strip(),
                        defaults={
                            'family': family,
                            'common_name': row['common_name'].strip(),
                            'slug': species_slug,
                            'description': row['description'].strip(),
                            'habitat': row['habitat'].strip(),
                            'diet': row['diet'].strip(),
                            'lifespan': row.get('life_span', '').strip(), 
                            'conservation_status': row.get('conservation_status', '').strip(), 
                            'geographical_scope': "Kerala Western Ghats"
                        }
                    )
                    
                    if created:
                        count += 1
                        
            self.stdout.write(self.style.SUCCESS(f"Success! Imported {count} real species from your CSV."))
            
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f"Could not find '{file_path}'. Make sure it is saved exactly next to your manage.py file."))
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f"Column header mismatch! Could not find the column: {e}. Please check your CSV headers."))