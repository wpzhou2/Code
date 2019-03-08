package com.weipeng.classschedule;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;


@SpringBootApplication
@MapperScan(value = "com.weipeng.classschedule.mapper")
public class ClassScheduleApplication {

    public static void main(String[] args) {
        SpringApplication.run(ClassScheduleApplication.class, args);
    }

}
