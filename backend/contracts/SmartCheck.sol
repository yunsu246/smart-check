pragma solidity ^0.4.24;

contract SmartCheck {
    
    struct Student {
        uint age;
        bytes fName;
        bytes lName;
        uint attendanceValue;
    }
    
    address public owner;
    
    mapping (uint => Student) studentList;
    uint[] public studIdList;
    
    event studentCreationEvent(
       bytes fName,
       bytes lName,
       uint age
    );
    
    function createStudent(uint _studId, uint _age, bytes _fName, bytes _lName) public {
        var student = studentList[_studId];
        
        student.age = _age;
        student.fName = _fName;
        student.lName = _lName;
        student.attendanceValue = 0;
        studIdList.push(_studId) -1;
        emit studentCreationEvent(_fName, _lName, _age);
    }
    
    function incrementAttendance(uint _studId) public {
        studentList[_studId].attendanceValue = studentList[_studId].attendanceValue+1;
    }
    
    function getStudents() view public returns(uint[]) {
        return studIdList;
    }
    
    function getParticularStudent(uint _studId) public view returns (bytes, bytes, uint, uint) {
        return (studentList[_studId].fName, studentList[_studId].lName, studentList[_studId].age, studentList[_studId].attendanceValue);
    }

    function countStudents() view public returns (uint) {
        return studIdList.length;
    }
    
}