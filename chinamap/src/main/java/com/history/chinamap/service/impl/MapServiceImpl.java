package com.history.chinamap.service.impl;

import com.history.chinamap.model.GeometryModel;
import com.history.chinamap.localcache.GeometryCache;
import com.history.chinamap.service.MapService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MapServiceImpl implements MapService {
    @Autowired
    private GeometryCache geometryCache;
    @Override
    public List<GeometryModel> getDynastyGeom(String category,Integer start, Integer end){
        return geometryCache.getDynastyGeometry(category,start,end);
    }
}
