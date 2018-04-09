// Delaunay Triangle: https://github.com/Bl4ckb0ne/delaunay-triangulation
// online test result: https://cl.ly/2T0r33001E46

#include <vector>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <map>

using namespace std;

template <typename T>
class Vector2
{
	public:
		//
		// Constructors
		//

		Vector2()
		{
			x = 0;
			y = 0;
		}

		Vector2(T _x, T _y) 
		{
			x = _x;
			y = _y;
		}

		Vector2(const Vector2 &v)
		{
			x = v.x;
			y = v.y;
		}

		void set(const Vector2 &v)
		{
			x = v.x;
			y = v.y;
		}

		//
		// Operations
		//	
		T dist2(const Vector2 &v)
		{
			T dx = x - v.x;
			T dy = y - v.y;
			return dx * dx + dy * dy;	
		}

		float dist(const Vector2 &v)
		{
			return sqrtf(dist2(v));
		}


		T x;
		T y;
};

template<typename T>
std::ostream &operator << (std::ostream &str, Vector2<T> const &point) 
{
    return str << "Point x: " << point.x << " y: " << point.y;
}

template<typename T>
bool operator == (Vector2<T> v1, Vector2<T> v2)
{
    return (v1.x == v2.x) && (v1.y == v2.y);
}

template <class T>
class Edge
{
	public:
		using VertexType = Vector2<T>;
		
		Edge(const VertexType &p1, const VertexType &p2) : p1(p1), p2(p2), isBad(false) {};
		Edge(const Edge &e) : p1(e.p1), p2(e.p2), isBad(false) {};

		VertexType p1;
		VertexType p2;

		bool isBad;
};

template <class T>
inline std::ostream &operator << (std::ostream &str, Edge<T> const &e)
{
	return str << "Edge " << e.p1 << ", " << e.p2;
}

template <class T>
inline bool operator == (const Edge<T> & e1, const Edge<T> & e2)
{
	return 	(e1.p1 == e2.p1 && e1.p2 == e2.p2) ||
			(e1.p1 == e2.p2 && e1.p2 == e2.p1);
}

template <class T>
class Triangle
{
	public:
		using EdgeType = Edge<T>;
		using VertexType = Vector2<T>;
		
		Triangle(const VertexType &_p1, const VertexType &_p2, const VertexType &_p3)
		:	p1(_p1), p2(_p2), p3(_p3),
			e1(_p1, _p2), e2(_p2, _p3), e3(_p3, _p1), isBad(false)
		{}
	
		bool containsVertex(const VertexType &v)
		{
			return p1 == v || p2 == v || p3 == v; 
		}
		
		bool circumCircleContains(const VertexType &v)
		{
			float ab = (p1.x * p1.x) + (p1.y * p1.y);
			float cd = (p2.x * p2.x) + (p2.y * p2.y);
			float ef = (p3.x * p3.x) + (p3.y * p3.y);

			float circum_x = (ab * (p3.y - p2.y) + cd * (p1.y - p3.y) + ef * (p2.y - p1.y)) / (p1.x * (p3.y - p2.y) + p2.x * (p1.y - p3.y) + p3.x * (p2.y - p1.y)) / 2.f;
			float circum_y = (ab * (p3.x - p2.x) + cd * (p1.x - p3.x) + ef * (p2.x - p1.x)) / (p1.y * (p3.x - p2.x) + p2.y * (p1.x - p3.x) + p3.y * (p2.x - p1.x)) / 2.f;
			float circum_radius = sqrtf(((p1.x - circum_x) * (p1.x - circum_x)) + ((p1.y - circum_y) * (p1.y - circum_y)));

			float dist = sqrtf(((v.x - circum_x) * (v.x - circum_x)) + ((v.y - circum_y) * (v.y - circum_y)));
			return dist <= circum_radius;
		}
	
		VertexType p1;
		VertexType p2;
		VertexType p3;
		EdgeType e1;				
		EdgeType e2;
		EdgeType e3;
		bool isBad;
};

template <class T>
inline std::ostream &operator << (std::ostream &str, const Triangle<T> & t)
{
	return str << "Triangle:" << std::endl << "\t" << t.p1 << std::endl << "\t" << t.p2 << std::endl << "\t" << t.p3 << std::endl << "\t" << t.e1 << std::endl << "\t" << t.e2 << std::endl << "\t" << t.e3 << std::endl;
		
}

template <class T>
inline bool operator == (const Triangle<T> &t1, const Triangle<T> &t2)
{
	return	(t1.p1 == t2.p1 || t1.p1 == t2.p2 || t1.p1 == t2.p3) &&
			(t1.p2 == t2.p1 || t1.p2 == t2.p2 || t1.p2 == t2.p3) && 
			(t1.p3 == t2.p1 || t1.p3 == t2.p2 || t1.p3 == t2.p3);
}

template <class T>
class Delaunay
{
	public:
		using TriangleType = Triangle<T>;
		using EdgeType = Edge<T>;
		using VertexType = Vector2<T>;
		
		const vector<TriangleType>& triangulate(vector<VertexType> &vertices)
		{
			// Store the vertices localy
			_vertices = vertices;

			// Determinate the super triangle
			float minX = vertices[0].x;
			float minY = vertices[0].y;
			float maxX = minX;
			float maxY = minY;

			for(size_t i = 0; i < vertices.size(); ++i) 
			{
				if (vertices[i].x < minX) minX = vertices[i].x;
		    	if (vertices[i].y < minY) minY = vertices[i].y;
		    	if (vertices[i].x > maxX) maxX = vertices[i].x;
		    	if (vertices[i].y > maxY) maxY = vertices[i].y;
			}
			
			float dx = maxX - minX;
			float dy = maxY - minY;
			float deltaMax = max(dx, dy);
			float midx = (minX + maxX) / 2.f;
			float midy = (minY + maxY) / 2.f;

			VertexType p1(midx - 20 * deltaMax, midy - deltaMax);
			VertexType p2(midx, midy + 20 * deltaMax);
			VertexType p3(midx + 20 * deltaMax, midy - deltaMax);	

			//cout << "Super triangle " << endl << Triangle(p1, p2, p3) << endl;
			
			// Create a list of triangles, and add the supertriangle in it
			_triangles.push_back(TriangleType(p1, p2, p3));

			for(auto p = begin(vertices); p != end(vertices); p++)
			{
				//cout << "Traitement du point " << *p << endl;
				//cout << "_triangles contains " << _triangles.size() << " elements" << endl;	

				vector<EdgeType> polygon;

				for(auto t = begin(_triangles); t != end(_triangles); t++)
				{
					//cout << "Processing " << endl << *t << endl;

					if(t->circumCircleContains(*p))
					{
						//cout << "Pushing bad triangle " << *t << endl;
						t->isBad = true;
						polygon.push_back(t->e1);	
						polygon.push_back(t->e2);	
						polygon.push_back(t->e3);	
					}
					else
					{
						//cout << " does not contains " << *p << " in his circum center" << endl;
					}
				}

				_triangles.erase(remove_if(begin(_triangles), end(_triangles), [](TriangleType &t){
					return t.isBad;
				}), end(_triangles));

				for(auto e1 = begin(polygon); e1 != end(polygon); e1++)
				{
					for(auto e2 = begin(polygon); e2 != end(polygon); e2++)
					{
						if(e1 == e2)
							continue;
						
						if(*e1 == *e2)
						{
							e1->isBad = true;
							e2->isBad = true;	
						}
					}
				}

				polygon.erase(remove_if(begin(polygon), end(polygon), [](EdgeType &e){
					return e.isBad;
				}), end(polygon));

				for(auto e = begin(polygon); e != end(polygon); e++)
					_triangles.push_back(TriangleType(e->p1, e->p2, *p));
			
			}

			_triangles.erase(remove_if(begin(_triangles), end(_triangles), [p1, p2, p3](TriangleType &t){
				return t.containsVertex(p1) || t.containsVertex(p2) || t.containsVertex(p3);
			}), end(_triangles));

			for(auto t = begin(_triangles); t != end(_triangles); t++)
			{
				_edges.push_back(t->e1);
				_edges.push_back(t->e2);
				_edges.push_back(t->e3);
			} 

			return _triangles;
		}
		
		const vector<TriangleType>& getTriangles() const { return _triangles; };
		const vector<EdgeType>& getEdges() const { return _edges; };
		const vector<VertexType>& getVertices() const { return _vertices; };

	private:
		vector<TriangleType> _triangles;
		vector<EdgeType> _edges;
		vector<VertexType> _vertices;
};

void readCoord(int N, vector<int>& coord) {
    for (int n = 0; n < N; ++n)
        scanf("%d", &coord[n]);
}

class QuickUnion {
	using Edge = pair<int, int>;
    vector<int> id, sz;

public:
    QuickUnion(int N) : id(N), sz(N, 1) {
        for (int n = 0; n < N; ++n) {
            id[n] = n;
        }
    }

    int size(int p) {
        return sz[p];
    }

    int find(int p) {
        while (p != id[p])
            p = id[p];
        return p;
    }

    bool connected(int p, int q) {
        return find(p) == find(q);
    }

    bool connected(Edge e) {
        return connected(e.first, e.second);
    }

    bool spanned(int p) {
        return sz[find(p)] == id.size();
    }

    bool spanned(Edge e) {
        return spanned(e.first);
    }

    bool unite(int p, int q) {
        int i = find(p);
        int j = find(q);

        if (i == j) return false;

        if (sz[i] >= sz[j]) {
            id[j] = i;
            sz[i] += sz[j];
        } else {
            id[i] = j;
            sz[j] += sz[i];
        }
        return true;
    }

    bool unite(Edge e) {
        return unite(e.first, e.second);
    }
};


double distance(Edge<double> e) {
	return sqrt(e.p1.dist2(e.p2));
}

using Dictionary = map<pair<int, int>, int>;
int findPointNumber(Dictionary& dict, Vector2<double> point) {
	auto pointPair = make_pair((int)point.x, (int)point.y);
	return dict[pointPair];
}

pair<int, int> edgeToPair(Dictionary& dict, Edge<double> e) {
	return make_pair(findPointNumber(dict, e.p1), findPointNumber(dict, e.p2));
}

int main() {
	int C;
    scanf("%d", &C);

    for (int c = 0; c < C; ++c) {
        int N, M;
        scanf("%d %d", &N, &M);

        vector<int> coordX(N), coordY(N);
        readCoord(N, coordX);
        readCoord(N, coordY);

		vector<Vector2<double> > points;
		Dictionary dict;
		for (int n = 0; n < N; ++n) {
			points.push_back(Vector2<double>(coordX[n], coordY[n]));
			dict[make_pair(coordX[n], coordY[n])] = n;
		}

		Delaunay<double> triangulation;
		vector<Triangle<double> > triangles = triangulation.triangulate(points);
		vector<Edge<double> > edges = triangulation.getEdges();

		auto qu = QuickUnion(N);
        for (int m = 0; m < M; ++m) {
            int a, b;
            scanf("%d %d", &a, &b);
            qu.unite(a, b);
        }

		vector<pair<double, pair<int, int> > > cand;
		for (auto e : edges) {
			double cost = distance(e);
			pair<int, int> edge = edgeToPair(dict, e);
			cand.push_back(make_pair(cost, edge));
		}

		sort(cand.begin(), cand.end());

		double totalDist = 0;
        for (auto p : cand) {
            double cost = p.first;
            pair<int, int> edge = p.second;


            if (qu.connected(edge)) continue;

            qu.unite(edge);
            totalDist += cost;

            if (qu.spanned(edge)) break;
        }

        printf("%.10f\n", totalDist);
	}
}