import unittest
from primaryMemory import PrimaryMemory
from secondaryMemory import SecondaryMemory
from sostructure import SOStructure
from action import Action
from file import File
from process import Process
from resource import Resources
from scheduler import Scheduler

class TestPrimaryMemory(unittest.TestCase):
    #@unittest.skip("teste1")
    def setUp(self):
        self.primaryMemory = PrimaryMemory(10,20)
        self.processes = {0:Process([2, 0, 3, 64, 0, 0, 0, 0]), 1:Process([2, 0, 3, 10, 0, 0, 0, 0]), 2:Process([2, 0, 3, 1, 0, 0, 0, 0]), 3:Process([2, 0, 3, 2, 0, 0, 0, 0]), 4:Process([2, 1, 3, 64, 0, 0, 0, 0]), 5:Process([2, 1, 3, 20, 0, 0, 0, 0]), 6:Process([2, 1, 3, 10, 0, 0, 0, 0]), 7:Process([2, 1, 3, 5, 0, 0, 0, 0]), 8:Process([2, 1, 3, 5, 0, 0, 0, 0]), 9:Process([2, 1, 3, 1, 0, 0, 0, 0]), 10:Process([2, 0, 3, 5, 0, 0, 0, 0]), 11:Process([2, 0, 3, 5, 0, 0, 0, 0]), 12:Process([2, 0, 3, 7, 0, 0, 0, 0])}

    def test_greater_total_size_real_time(self):
        result = self.primaryMemory.addProcess(self.processes[0], 0)
        self.assertEqual(result,2)
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[])

    def test_greater_total_size_user(self):
        result = self.primaryMemory.addProcess(self.processes[4], 4)
        self.assertEqual(result,2)
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[])

    def test_equal_total_size_real_time(self):
        result = self.primaryMemory.addProcess(self.processes[1], 1)
        self.assertEqual(result,0)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, {1:(0,10)})

    def test_equal_total_size_user(self):
        result = self.primaryMemory.addProcess(self.processes[5], 5)
        self.assertEqual(result,0)
        self.assertEqual(self.primaryMemory.freeUserMemory, {})
        self.assertEqual(self.primaryMemory.busyUserMemory, {5:(0,20)})

    def test_less_total_size_real_time(self):
        result = self.primaryMemory.addProcess(self.processes[2], 2)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[3], 3)
        self.assertEqual(result,0)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {3:7})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, {2:(0,1), 3:(1,2)})

    def test_less_total_size_user(self):
        result = self.primaryMemory.addProcess(self.processes[6], 6)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[7], 7)
        self.assertEqual(result,0)
        self.assertEqual(self.primaryMemory.freeUserMemory, {15:5})
        self.assertEqual(self.primaryMemory.busyUserMemory, {6:(0,10), 7:(10,5)})

    def test_full_real_time_1(self):
        result = self.primaryMemory.addProcess(self.processes[10], 10)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[11], 11)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[2], 2)
        self.assertEqual(result,1)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, {10:(0,5), 11:(5,5)})
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[(2,self.processes[2])])

    def test_full_user_1(self):
        result = self.primaryMemory.addProcess(self.processes[6], 6)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[7], 7)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[8], 8)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[9], 9)
        self.assertEqual(result,1)
        self.assertEqual(self.primaryMemory.freeUserMemory, {})
        self.assertEqual(self.primaryMemory.busyUserMemory, {6:(0,10), 7:(10,5), 8:(15,5)})
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[(9,self.processes[9])])

    def test_full_real_time_2(self):
        result = self.primaryMemory.addProcess(self.processes[10], 10)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[11], 11)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[2], 2)
        self.assertEqual(result,1)
        result = self.primaryMemory.addProcess(self.processes[3], 3)
        self.assertEqual(result,1)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, {10:(0,5), 11:(5,5)})
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[(2,self.processes[2]), (3,self.processes[3])])

    def test_full_user_2(self):
        result = self.primaryMemory.addProcess(self.processes[6], 6)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[7], 7)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[8], 8)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[9], 9)
        self.assertEqual(result,1)
        result = self.primaryMemory.addProcess(self.processes[5], 5)
        self.assertEqual(result,1)
        self.assertEqual(self.primaryMemory.freeUserMemory, {})
        self.assertEqual(self.primaryMemory.busyUserMemory, {6:(0,10), 7:(10,5), 8:(15,5)})
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[(9,self.processes[9]), (5,self.processes[5])])

    def test_delete_real_time1(self):
        result = self.primaryMemory.addProcess(self.processes[2], 2)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[3], 3)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[12], 12)
        self.assertEqual(result,0)
        self.primaryMemory.removeProcess(self.processes[3], 3)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {1:2})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, {2:(0,1), 12:(3,7)})

    def test_delete_user1(self):
        result = self.primaryMemory.addProcess(self.processes[6], 6)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[7], 7)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[8], 8)
        self.assertEqual(result,0)
        self.primaryMemory.removeProcess(self.processes[7], 7)
        self.assertEqual(self.primaryMemory.freeUserMemory, {10:5})
        self.assertEqual(self.primaryMemory.busyUserMemory, {6:(0,10), 8:(15,5)})

    def test_delete_real_time_2(self):
        result = self.primaryMemory.addProcess(self.processes[2], 2)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[3], 3)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[12], 12)
        self.assertEqual(result,0)
        self.primaryMemory.removeProcess(self.processes[2], 2)
        self.primaryMemory.removeProcess(self.processes[3], 3)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {0:3})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, { 12:(3,7)})

    def test_delete_user_2(self):
        result = self.primaryMemory.addProcess(self.processes[6], 6)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[7], 7)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[8], 8)
        self.assertEqual(result,0)
        self.primaryMemory.removeProcess(self.processes[6], 6)
        self.primaryMemory.removeProcess(self.processes[7], 7)
        self.assertEqual(self.primaryMemory.freeUserMemory, {0:15})
        self.assertEqual(self.primaryMemory.busyUserMemory, {8:(15,5)})

    def test_delete_real_time_3(self):
        result = self.primaryMemory.addProcess(self.processes[2], 2)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[3], 3)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[12], 12)
        self.assertEqual(result,0)
        self.primaryMemory.removeProcess(self.processes[3], 3)
        self.primaryMemory.removeProcess(self.processes[2], 2)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {0:3})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, { 12:(3,7)})

    def test_delete_user_3(self):
        result = self.primaryMemory.addProcess(self.processes[6], 6)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[7], 7)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[8], 8)
        self.assertEqual(result,0)
        self.primaryMemory.removeProcess(self.processes[7], 7)
        self.primaryMemory.removeProcess(self.processes[6], 6)
        self.assertEqual(self.primaryMemory.freeUserMemory, {0:15})
        self.assertEqual(self.primaryMemory.busyUserMemory, {8:(15,5)})

    def test_delete_real_time_all(self):
        result = self.primaryMemory.addProcess(self.processes[2], 2)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[3], 3)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[12], 12)
        self.assertEqual(result,0)
        self.primaryMemory.removeProcess(self.processes[2], 2)
        self.primaryMemory.removeProcess(self.processes[3], 3)
        self.primaryMemory.removeProcess(self.processes[12], 12)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {0:10})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, {})

    def test_delete_user_all(self):
        result = self.primaryMemory.addProcess(self.processes[6], 6)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[7], 7)
        self.assertEqual(result,0)
        result = self.primaryMemory.addProcess(self.processes[8], 8)
        self.assertEqual(result,0)
        self.primaryMemory.removeProcess(self.processes[6], 6)
        self.primaryMemory.removeProcess(self.processes[7], 7)
        self.primaryMemory.removeProcess(self.processes[8], 8)
        self.assertEqual(self.primaryMemory.freeUserMemory, {0:20})
        self.assertEqual(self.primaryMemory.busyUserMemory, {})

    def test_retry_allocation_real_time(self):
        result = self.primaryMemory.addProcess(self.processes[10], 10)
        result = self.primaryMemory.addProcess(self.processes[11], 11)
        result = self.primaryMemory.addProcess(self.processes[2], 2)
        self.primaryMemory.removeProcess(self.processes[11], 11)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {6:4})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, {10:(0,5), 2:(5,1)})
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[])

    def test_retry_allocation_user(self):
        result = self.primaryMemory.addProcess(self.processes[6], 6)
        result = self.primaryMemory.addProcess(self.processes[7], 7)
        result = self.primaryMemory.addProcess(self.processes[8], 8)
        result = self.primaryMemory.addProcess(self.processes[9], 9)
        self.primaryMemory.removeProcess(self.processes[7], 7)
        self.assertEqual(self.primaryMemory.freeUserMemory, {11:4})
        self.assertEqual(self.primaryMemory.busyUserMemory, {6:(0,10), 9:(10,1), 8:(15,5)})
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[])

    def test_fail_retry_allocation_real_time(self):
        result = self.primaryMemory.addProcess(self.processes[10], 10)
        result = self.primaryMemory.addProcess(self.processes[2], 2)
        result = self.primaryMemory.addProcess(self.processes[3], 3)
        result = self.primaryMemory.addProcess(self.processes[11], 11)
        self.primaryMemory.removeProcess(self.processes[2], 2)
        self.assertEqual(self.primaryMemory.freeRealTimeMemory, {5:1, 8:2})
        self.assertEqual(self.primaryMemory.busyRealTimeMemory, {10:(0,5), 3:(6,2)})
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[(11,self.processes[11])])

    def test_fail_retry_allocation_user(self):
        result = self.primaryMemory.addProcess(self.processes[6], 6)
        result = self.primaryMemory.addProcess(self.processes[9], 9)
        result = self.primaryMemory.addProcess(self.processes[7], 7)
        result = self.primaryMemory.addProcess(self.processes[8], 8)
        self.primaryMemory.removeProcess(self.processes[9], 9)
        self.assertEqual(self.primaryMemory.freeUserMemory, {10:1,16:4})
        self.assertEqual(self.primaryMemory.busyUserMemory, {6:(0,10), 7:(11,5)})
        self.assertEqual(self.primaryMemory.notAllocatedProcess,[(8,self.processes[8])])

class TestSecondaryMemory(unittest.TestCase):
    #@unittest.skip("teste1")
    def setUp(self):
        self.secondaryMemory = SecondaryMemory(10)
        self.files = {'A':File(['A',20]),'B':File(['B',10]),'C':File(['C',5]),'D':File(['C',2]),'E':File(['E',5]),'F':File(['F',2]),'G':File(['G',2]),'H':File(['H',7]),'I':File(['I',2]),'J':File(['J',2])}

    def test_same_name_file_1(self):
        result = self.secondaryMemory.addFile(self.files['C'])
        self.assertEqual(result, 0)
        result = self.secondaryMemory.addFile(self.files['D'])
        self.assertEqual(result, 2)

    def test_same_name_file_2(self):
        result = self.secondaryMemory.addFile(self.files['C'])
        self.assertEqual(result, 0)
        self.secondaryMemory.removeFile('C')
        result = self.secondaryMemory.addFile(self.files['D'])
        self.assertEqual(result, 0)

    def test_start_position(self):
        result = self.secondaryMemory.addFile(self.files['J'], 4)
        self.assertEqual(result, 0)
        self.assertEqual(self.secondaryMemory.freeMemory,{0:4,6:4})
        self.assertEqual(self.secondaryMemory.busyMemory,{'J':(4,2)})

    def test_greater_total_size(self):
        result = self.secondaryMemory.addFile(self.files['A'])
        self.assertEqual(result,1)


    def test_equal_total_size(self):
        result = self.secondaryMemory.addFile(self.files['B'])
        self.assertEqual(result,0)
        self.assertEqual(self.secondaryMemory.freeMemory, {})
        self.assertEqual(self.secondaryMemory.busyMemory, {'B':(0,10)})


    def test_less_total_size(self):
        result = self.secondaryMemory.addFile(self.files['F'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['G'])
        self.assertEqual(result,0)
        self.assertEqual(self.secondaryMemory.freeMemory, {4:6})
        self.assertEqual(self.secondaryMemory.busyMemory, {'F':(0,2), 'G':(2,2)})

    def test_full(self):
        result = self.secondaryMemory.addFile(self.files['C'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['E'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['F'])
        self.assertEqual(result,1)
        self.assertEqual(self.secondaryMemory.freeMemory, {})
        self.assertEqual(self.secondaryMemory.busyMemory, {'C':(0,5), 'E':(5,5)})

    def test_delete_1(self):
        result = self.secondaryMemory.addFile(self.files['E'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['F'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['G'])
        self.assertEqual(result,0)
        self.secondaryMemory.removeFile('F')
        self.assertEqual(self.secondaryMemory.freeMemory, {5:2, 9:1})
        self.assertEqual(self.secondaryMemory.busyMemory, {'E':(0,5), 'G':(7,2)})


    def test_delete_2(self):
        result = self.secondaryMemory.addFile(self.files['E'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['F'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['G'])
        self.assertEqual(result,0)
        self.secondaryMemory.removeFile('E')
        self.secondaryMemory.removeFile('F')
        self.assertEqual(self.secondaryMemory.freeMemory, {0:7, 9:1})
        self.assertEqual(self.secondaryMemory.busyMemory, { 'G':(7,2)})

    def test_delete_3(self):
        result = self.secondaryMemory.addFile(self.files['E'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['F'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['G'])
        self.assertEqual(result,0)
        self.secondaryMemory.removeFile('F')
        self.secondaryMemory.removeFile('E')
        self.assertEqual(self.secondaryMemory.freeMemory, {0:7, 9:1})
        self.assertEqual(self.secondaryMemory.busyMemory, { 'G':(7,2)})

    def test_delete_all(self):
        result = self.secondaryMemory.addFile(self.files['C'])
        self.assertEqual(result,0)
        result = self.secondaryMemory.addFile(self.files['E'])
        self.assertEqual(result,0)
        self.secondaryMemory.removeFile('C')
        self.secondaryMemory.removeFile('E')
        self.assertEqual(self.secondaryMemory.freeMemory, {0:10})
        self.assertEqual(self.secondaryMemory.busyMemory, {})

class TestResources(unittest.TestCase):
    def setUp(self):
        self.resources = Resources()
        self.process = Process([2, 0, 3, 64, 0, 0, 0, 0],1)

    def test_allocation_success(self):
        result = self.resources.requestResources([1,0,0,1],1)
        self.assertEqual(result,True)
        self.assertEqual(self.resources.busyResource,{'printer':[1], 'scanner':[], 'modem':[], 'disk':[1]})
        self.process.requestResources(self.resources)

    def test_allocation_fail(self):
        result = self.resources.requestResources([1,1,1,1],1)
        self.assertEqual(result,True)
        result = self.resources.requestResources([1,1,1,1],0)
        self.assertEqual(result,False)

class TestActions(unittest.TestCase):
    def setUp(self):
        self.secondaryMemory = SecondaryMemory(10)
        self.processes = {0:Process([2, 0, 3, 64, 0, 0, 0, 0]), 1:Process([2, 0, 3, 10, 0, 0, 0, 0]), 2:Process([2, 0, 3, 1, 0, 0, 0, 0]), 3:Process([2, 0, 0, 2, 0, 0, 0, 0]), 4:Process([2, 1, 3, 64, 0, 0, 0, 0]), 5:Process([2, 1, 3, 20, 0, 0, 0, 0]), 6:Process([2, 1, 3, 10, 0, 0, 0, 0]), 7:Process([2, 1, 3, 5, 0, 0, 0, 0]), 8:Process([2, 1, 3, 5, 0, 0, 0, 0]), 9:Process([2, 1, 3, 1, 0, 0, 0, 0]), 10:Process([2, 0, 3, 5, 0, 0, 0, 0]), 11:Process([2, 0, 3, 5, 0, 0, 0, 0]), 12:Process([2, 0, 3, 7, 0, 0, 0, 0])}
        self.actions = {0:[Action([0,0,'A',3,0]),Action([0,0,'A',3,1]),Action([0,1,'B',2]),Action([0,1,'A',3]) ],1:[Action([0,0,'A',3,0]),Action([0,0,'A',3,1]),Action([0,1,'B',2])]}
    def test_error_action_timeout(self):
         result = SOStructure.execAction(self, self.actions[0][0], self.processes[3], self.secondaryMemory)
         self.assertEqual(result,1)
    def test_ok_action(self):
         result = SOStructure.execAction(self, self.actions[1][0], self.processes[0], self.secondaryMemory)
         self.assertEqual(result,0)

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = Scheduler()
        self.processes = {0:Process([0, 1, 3, 64, 0, 0, 0, 0]), 1:Process([1, 0, 3, 10, 0, 0, 0, 0]), 2:Process([0, 2, 3, 1, 0, 0, 0, 0]), 3:Process([0, 3, 0, 2, 0, 0, 0, 0]), 4:Process([2, 0, 3, 64, 0, 0, 0, 0]), 5:Process([2, 1, 3, 20, 0, 0, 0, 0]), 6:Process([2, 1, 3, 10, 0, 0, 0, 0]), 7:Process([2, 1, 3, 5, 0, 0, 0, 0]), 8:Process([2, 1, 3, 5, 0, 0, 0, 0]), 9:Process([2, 1, 3, 1, 0, 0, 0, 0]), 10:Process([2, 0, 3, 5, 0, 0, 0, 0]), 11:Process([2, 0, 3, 5, 0, 0, 0, 0]), 12:Process([2, 0, 3, 7, 0, 0, 0, 0])}

    def test_queueProcess_ok(self):
         result1 = self.scheduler.queueProcess(self.processes[0])
         result2 = self.scheduler.queueProcess(self.processes[1])
         result3 = self.scheduler.queueProcess(self.processes[2])
         result4 = self.scheduler.queueProcess(self.processes[3])
         self.assertEqual(result4,0)

    def test_scheduleProcess_ok(self):
         result1 = self.scheduler.queueProcess(self.processes[0])
         result2 = self.scheduler.queueProcess(self.processes[1])
         result3 = self.scheduler.queueProcess(self.processes[2])
         result4 = self.scheduler.queueProcess(self.processes[3])
         result4 = self.scheduler.queueProcess(self.processes[4])

         process = self.scheduler.scheduleProcess()
         process = self.scheduler.scheduleProcess()
         result = (process == self.processes[4])
         self.assertEqual(result,True)

    def test_preemptProcess1_ok(self):
         result1 = self.scheduler.queueProcess(self.processes[0])
         process = self.scheduler.scheduleProcess()
         result2 = self.scheduler.queueProcess(self.processes[1])
         process2 = self.scheduler.preemptProcess(process,1)

         result = (process2 == self.processes[1])
         self.assertEqual(result,True)

    def test_preemptProcess2_ok(self):
         result1 = self.scheduler.queueProcess(self.processes[2])
         process = self.scheduler.scheduleProcess()
         result2 = self.scheduler.queueProcess(self.processes[0])
         process2 = self.scheduler.preemptProcess(process,1)

         result = (process2 == self.processes[0])
         self.assertEqual(result,True)


class TestSO(unittest.TestCase):
    def setUp(self):
        self.soStructure = SOStructure("")
        # self.secondaryMemory = SecondaryMemory(10)
        self.processes = {0:Process([2, 0, 3, 64, 0, 0, 0, 0]), 1:Process([3, 0, 4, 64, 0, 0, 0, 0])}
        # self.actions = {0:[Action([0,0,'A',3,0]),Action([0,0,'A',3,1]),Action([0,1,'B',2]),Action([0,1,'A',3]) ],1:[Action([0,0,'A',3,0]),Action([0,0,'A',3,1]),Action([0,1,'B',2])]}

    def test_assemble_ok(self):
        self.assertEqual(self.soStructure.processes, self.processes)

    @unittest.skip("pra não fazer agora")
    def test_run_ok(self):
        result = self.soStructure.run()

        self.assertEqual(result,0)

if __name__ == '__main__':
    unittest.main()
