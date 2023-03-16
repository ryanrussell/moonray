// Copyright 2023 DreamWorks Animation LLC
// SPDX-License-Identifier: Apache-2.0

/// @file TestBsdfv.h

#pragma once

#include <cppunit/extensions/HelperMacros.h>
#include <cppunit/TestFixture.h>

namespace moonray {
namespace pbr {
///
/// @class TestBsdfv TestBsdfv.h <pbr/unittest/TestBsdfv.h>
/// @brief This class tests response and statistical properties of all the
/// vectorized bsdf models we have in lib/pbr.  It is analogous to the
/// BsdfSampler and BsdfOneSampler scalar tests.
///
class TestBsdfv : public CppUnit::TestFixture
{
public:
    TestBsdfv();
    ~TestBsdfv();

    void setUp();
    void tearDown();

    CPPUNIT_TEST_SUITE(TestBsdfv);
#if 1
    CPPUNIT_TEST(testLambert);

    CPPUNIT_TEST(testCookTorrance);
    CPPUNIT_TEST(testGGXCookTorrance);
    CPPUNIT_TEST(testAnisoCookTorrance);
    CPPUNIT_TEST(testTransmissionCookTorrance);

    CPPUNIT_TEST(testIridescence);

    CPPUNIT_TEST(testRetroreflection);

    CPPUNIT_TEST(testEyeCaustic);

    CPPUNIT_TEST(testDwaFabric);
    CPPUNIT_TEST(testKajiyaKayFabric);

    CPPUNIT_TEST(testAshikhminShirley);
    CPPUNIT_TEST(testAshikhminShirleyFull);

    CPPUNIT_TEST(testWardCorrected);
    CPPUNIT_TEST(testWardDuer);

    CPPUNIT_TEST(testHairDiffuse);
    CPPUNIT_TEST(testHairR);
    CPPUNIT_TEST(testHairTT);

    CPPUNIT_TEST(testTwoLobes);
    CPPUNIT_TEST(testThreeLobes);
    CPPUNIT_TEST(testStochasticFlakes);
#endif
    CPPUNIT_TEST_SUITE_END();

    void testLambert();

    void testCookTorrance();
    void testGGXCookTorrance();
    void testAnisoCookTorrance();
    void testTransmissionCookTorrance();

    void testIridescence();

    void testRetroreflection();

    void testEyeCaustic();

    void testDwaFabric();
    void testKajiyaKayFabric();

    void testAshikhminShirley();
    void testAshikhminShirleyFull();

    void testWardCorrected();
    void testWardDuer();

    void testHairDiffuse();
    void testHairR();
    void testHairTT();

    void testTwoLobes();
    void testThreeLobes();
    void testStochasticFlakes();
};

} // namespace pbr
} // namespace moonray


