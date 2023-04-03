package com.history.chinamap.service;

import com.history.chinamap.model.GeometryModel;

import java.util.List;

public interface MapService {
    List<GeometryModel> getDynastyGeom(String category,Integer start,Integer end);
}