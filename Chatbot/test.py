import core_skills as Core
import myparamiko as paramiko

# Testing to get datetime from function

router = 'r2'
router_dict = Core.router_select(router)
print(router_dict)

for k, v in router_dict.items():
    print(f"{k}:{v}")