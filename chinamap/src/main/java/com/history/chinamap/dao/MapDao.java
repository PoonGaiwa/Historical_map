package com.history.chinamap.dao;

import com.history.chinamap.model.GeometryModel;
import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Service;

@Service

public interface MapDao {
    GeometryModel getCntyPoint(@Param("gId") Integer gId);
    GeometryModel getPrefPoint(@Param("gId") Integer gId);
    GeometryModel getPrefPolygon(@Param("gId") Integer gId);
}