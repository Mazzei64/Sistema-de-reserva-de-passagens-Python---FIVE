from backend.entities.auth import Auth
from backend.entities.user_route import User_Route

class Repository:
    def __init__(self):
        self.__userRepo = []
        self.__authKey = []
        self.__User_Route = []
        
    
    #CRUD PARA USER
    def CreateUser(self, user):
        lastId = self.GetLastUsersID()
        user.id = lastId + 1
        return self.__userRepo.append(user)
    
    def GetUser(id):
        return None
    
    def GetAllUsers(self):
        return self.__userRepo
    
    def UpdateUser(id):
        return None
    
    def DeleteUser(self, id):
        self.__userRepo.remove({ id })
    
    def GetLastUsersID(self):
        len = self.__userRepo.__len__()
        if(len == 0):
            return 0
        
        user = self.__userRepo[len - 1]
        return user.id
    
    def FindUserByEmail(self, email):
        for i in range(self.__userRepo.__len__()):
            if (self.__userRepo[i].email == email):
                return self.__userRepo[i]
        
        return None
    
    def AuthUser(self, authKey):
        key = Auth()
        key.userId = authKey.userId
        key.token = authKey.token
        self.__authKey.append(key)
    
    def IsAuthUser(self, authKey):
        if self.__authKey.__len__() == 0:
            return False
        
        for i in range(self.__authKey.__len__()):
            if self.__authKey[i].token == authKey.token:
                return True
        
        return False
    
    def RemoveAuthUser(self, authKey):
        self.__authKey.pop()
        authKey.userId = 0
        authKey.token = ""
    
    def AssignRouteToUser(self, route, userId):
        user_route = User_Route()
        user_route.id = self.GetLastUser_RouteID() + 1
        user_route.userId = userId
        user_route.route = route
        self.__User_Route.append(user_route)
    
    def GetLastUser_RouteID(self):
        len = self.__User_Route.__len__()
        if(len == 0):
            return 0
        
        user_route = self.__User_Route[len - 1]
        return user_route.id
    
    def GetRoustesListByUserId(self, list, userId):
        
        if self.__User_Route.__len__() == 0:
            return 0
        
        for i in range(self.__User_Route.__len__()):
            if self.__User_Route[i].userId == userId:
                list.append(self.__User_Route[i].route)
        return 1
    
    def GetRouteByUserId(self, userId):
        if self.__User_Route.__len__() == 0:
            return None
        
        for i in range(self.__User_Route.__len__()):
            if self.__User_Route[i].userId == userId:
                return self.__User_Route[i].route
        
        return None
    
    def UserHasRoutes(self, userId):
        if self.GetRouteByUserId(userId) == None:
            return False
        
        return True