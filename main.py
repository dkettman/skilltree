#####
# Skill Tree
# By Dave Kettmann <david.kettmann@gmail.com>
#
# Purpose: Intended to be used with a Discord bot to help facilitate storing
#          builds and accessing via a #build type channel
#####

class Skill:

    def __init__(self,skill_class,skill_tree,skill_name,level_req,parent,children):
        self.skill_class = skill_class
        self.skill_tree = skill_tree
        self.skill_name = skill_name
        self.level_req = level_req
        self.parent = parent
        self.children = children


    def print(self):
        print("Skill Class:  %s" % self.skill_class)
        print("Skill Tree:   %s" % self.skill_tree)
        print("Skill Name:   %s" % self.skill_name)
        print("Skill Level:  %s" % self.level_req)
        print("Parent Skill: %s" % self.parent)
        print("Children:     %s" % self.children)


foo = Skill("Viking","Shield Bearer","Recovery",1,None,["Odin's Fury"])
foo.print()
