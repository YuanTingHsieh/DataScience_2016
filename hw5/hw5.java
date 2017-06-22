import weka.core.converters.ConverterUtils.DataSource;
import weka.core.Instances;
//import java.io.BufferedReader;
//import java.io.FileReader;

import weka.filters.Filter;
import weka.filters.unsupervised.attribute.StringToWordVector;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.trees.J48;
import weka.classifiers.Evaluation;

public class hw5{

    public static void main(String[] args) {
        try
        {
            DataSource trainsource = new DataSource("./ReutersCorn-train.arff");
            DataSource testsource = new DataSource("./ReutersCorn-test.arff");
            Instances traindata = trainsource.getDataSet();
            Instances testdata = testsource.getDataSet();
            traindata.setClassIndex(traindata.numAttributes() -1 );
            testdata.setClassIndex(testdata.numAttributes() -1 );

            StringToWordVector filter = new StringToWordVector();
            filter.setInputFormat(traindata);
            traindata = Filter.useFilter(traindata,filter);
            testdata = Filter.useFilter(testdata,filter);

            NaiveBayes nb = new NaiveBayes();
            nb.buildClassifier(traindata);
            Evaluation eval = new Evaluation(traindata);
            eval.evaluateModel(nb, testdata);
            System.out.println(eval.toSummaryString("\nResults\n======\n", false));

            J48 cls = new J48();
            cls.buildClassifier(traindata);
            eval = new Evaluation(traindata);
            eval.evaluateModel(cls, testdata);
            System.out.println(eval.toSummaryString("\nResults\n======\n", false));

        } catch (Exception e){
            e.printStackTrace();
        }
    }
}
