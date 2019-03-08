package com.weipeng.classschedule.controller;

import com.weipeng.classschedule.bean.Course;
import com.weipeng.classschedule.mapper.CourseMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

/**
 * @Author: weipeng
 * @Date: 2019/3/3  22:37
 * @Description:
 **/
@RestController
public class CourseController {
    @Autowired
    CourseMapper courseMapper;

    @GetMapping("/getCoursesByStudentName/{studentName}")
    public List<Course> getCoursesByStudentName(@PathVariable("studentName") String studentName){
        return courseMapper.getCoursesByStudentName(studentName);
    }

    @GetMapping("/getCoursesByStudentID/{studentID}")
    public List<Course> getCoursesByStudentID(@PathVariable("studentID") String studentID){
        return courseMapper.getCoursesByStudentID(studentID);
    }

}
