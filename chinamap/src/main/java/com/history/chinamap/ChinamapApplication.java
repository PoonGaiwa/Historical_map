package com.history.chinamap;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.history.chinamap.dao")

public class ChinamapApplication {

    public static void main(String[] args) {
        SpringApplication.run(ChinamapApplication.class, args);
    }

}
