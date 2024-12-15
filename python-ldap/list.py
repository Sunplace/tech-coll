import ldap
import json

ldapconn = ldap.initialize('ldap://10.254.15.1:389')

# r = ldapconn.simple_bind_s('cn=gitlab, OU=services, OU=Users, OU=corp, DC=xi, DC=local', 'X8')
r = ldapconn.simple_bind_s('CN=Yun,OU=平台研发组,OU=软件研发部,OU=自动化研发部,OU=AI,OU=i,OU=Users,OU=corp,DC=i,DC=local', 'MP')
searchScope = ldap.SCOPE_SUBTREE
# searchFilter = 'cn=YSun'
# searchFilter = 'cn=Pao'
# searchFilter = "(memberOf=CN=平台开发部,OU=软件研发部,OU=自动化研发部,OU=AI,OU=i,OU=Users,OU=corp,DC=pi,DC=local)"
searchFilter = '''(&
    (memberOf=CN=平台开发部,OU=软件研发部,OU=自动化研发部,OU=I,OU=i,OU=Users,OU=corp,DC=i,DC=local)
    (objectclass=person)
)'''
base_dn = 'OU=Users, OU=corp, DC=x, DC=local'
# print(ldapconn.search_s(base_dn, searchScope, searchFilter, None))
for user in ldapconn.search_s(base_dn, searchScope, searchFilter, None):
    user_info = user[1]
    print(user_info['cn'])
    # exit(0)
