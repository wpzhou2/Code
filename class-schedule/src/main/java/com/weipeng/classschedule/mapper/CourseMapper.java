package com.weipeng.classschedule.mapper;

import com.weipeng.classschedule.bean.Course;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;

/**
 * @Author: weipeng
 * @Date: 2019/3/3  22:24
 * @Description:
 **/
@Mapper
public interface CourseMapper {
    @Select("select * from courses2 where studentName = #{studentName}")
    public List<Course> getCoursesByStudentName(String studentName);

    @Select("select * from courses2 where studentID = #{studentID}")
    public List<Course> getCoursesByStudentID(String studentID);

}
