package com.history.chinamap.model;

import org.locationtech.jts.geom.Geometry;
import lombok.Getter;
import lombok.Setter;
import lombok.ToString;

@Getter
@Setter
@ToString

public class GeometryModel {
    private Integer gId;
    private String namePy;
    private String nameCh;
    private String nameFt;
    private String presLoc;
    private String typePy;
    private String typeCh;
    private String levRank;
    private Integer begYr;
    private String begRule;
    private Integer endYr;
    private String endRule;
    private String geoSrc;
    private String compiler;
    private String gecomplr;
    private String checker;
    private String entDate;
    private String begChgTy;
    private String endChgTy;
    private Geometry geometry;

    public String getNamePy() {
        return namePy;
    }
    public String getNameCh() {
        return nameCh;
    }
    public Geometry getGeometry() {
        return geometry;
    }
    public String getNameFt() {
        return nameFt;
    }
    public String getPresLoc() {
        return presLoc;
    }
    public String getTypePy() {
        return typePy;
    }
    public String getTypeCh() {
        return typeCh;
    }
    public String getLevRank() {
        return levRank;
    }
    public Integer getBegYr() {
        return begYr;
    }
    public String getBegRule() {
        return begRule;
    }
    public Integer getEndYr() {
        return endYr;
    }
    public String getEndRule() {
        return endRule;
    }
    public String getGeoSrc() {
        return geoSrc;
    }
    public String getCompiler() {
        return compiler;
    }
    public String getGecomplr() {
        return gecomplr;
    }
    public String getChecker() {
        return checker;
    }
    public String getEntDate() {
        return entDate;
    }
    public String getBegChgTy() {
        return begChgTy;
    }
    public String getEndChgTy() {
        return endChgTy;
    }
    public Integer getGid() {
        return gId;
    }


//    public void setGid(Integer gId) {
//        this.gId=gId;
//    }
//    public void setNamePy(String namePy) {
//        this.namePy = namePy;
//    }
//    public void setNameCh(String nameCh) {
//        this.nameCh=nameCh;
//    }
//    public void setBegChgTy(String begChgTy) {
//        this.begChgTy = begChgTy;
//    }
//    public void setBegRule(String begRule) {
//        this.begRule = begRule;
//    }
//    public void setBegYr(Integer begYr) {
//        this.begYr = begYr;
//    }
//    public void setChecker(String checker) {
//        this.checker = checker;
//    }
//    public void setCompiler(String compiler) {
//        this.compiler = compiler;
//    }
//    public void setEndChgTy(String endChgTy) {
//        this.endChgTy = endChgTy;
//    }
//    public void setEndYr(Integer endYr) {
//        this.endYr = endYr;
//    }
//    public void setEndRule(String endRule) {
//        this.endRule = endRule;
//    }
//    public void setEntDate(String entDate) {
//        this.entDate = entDate;
//    }
//    public void setGecomplr(String gecomplr) {
//        this.gecomplr = gecomplr;
//    }
//    public void setGeoSrc(String geoSrc) {
//        this.geoSrc = geoSrc;
//    }
//    public void setgId(Integer gId) {
//        this.gId = gId;
//    }
//    public void setLevRank(String levRank) {
//        this.levRank = levRank;
//    }
//    public void setNameFt(String nameFt) {
//        this.nameFt = nameFt;
//    }
//    public void setPresLoc(String presLoc) {
//        this.presLoc = presLoc;
//    }
//    public void setTypeCh(String typeCh) {
//        this.typeCh = typeCh;
//    }
//    public void setTypePy(String typePy) {
//        this.typePy = typePy;
//    }
//    public void setGeometry(Geometry geometry) {
//        this.geometry=geometry;
//    }

}
