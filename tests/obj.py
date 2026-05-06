import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/root/stepik_assistent')))


from app.models.project import ObjectsTypes


print(ObjectsTypes().objects)